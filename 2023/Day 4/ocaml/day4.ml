open Core

let safe_int_of_string s =
  try Some (Int.of_string s)
  with Failure _ -> None

let read_lines filename =
  In_channel.with_file filename ~f:(fun file ->
      In_channel.fold_lines file ~init:[] ~f:(fun acc line ->
          match String.split line ~on:'|' with
          | [winning; mine] ->
            let winning_numbers = String.split winning ~on:' ' |> List.filter_map ~f:safe_int_of_string in
            let mine_numbers = String.split mine ~on:' ' |> List.filter_map ~f:safe_int_of_string in
            (winning_numbers, mine_numbers) :: acc
          | _ -> acc
        )
    )
  |> List.rev

let calculate_total_points cards =
  List.fold cards ~init:0 ~f:(fun acc (winning, mine) ->
      let matches = List.length (List.filter winning ~f:(List.mem mine ~equal:Int.equal)) in
      if matches > 0 then acc + (1 lsl (matches - 1)) else acc
    )
let calculate_total_scratchcards cards =
  let n = List.length cards in
  let instances = Array.create ~len:n 1 in
  let matches = List.map cards ~f:(fun (winning, mine) ->
      List.length (List.filter winning ~f:(List.mem mine ~equal:Int.equal))
    ) in
  List.iteri matches ~f:(fun i match_count ->
      for j = i + 1 to min (i + match_count) (n - 1) do
        instances.(j) <- instances.(j) + instances.(i)
      done
    );
  Array.fold instances ~init:0 ~f:(+)

let () =
  let argv = Sys.get_argv () in
  if Array.length argv < 2 then (
    Printf.eprintf "Usage: %s <filename>\n" argv.(0);
    exit 1
  );
  let filename = argv.(1) in
  let cards = read_lines filename in
  let total_points = calculate_total_points cards in
  Printf.printf "Total Points: %d\n" total_points;
  let total_scratchcards = calculate_total_scratchcards cards in
  Printf.printf "Total Scratchcards: %d\n" total_scratchcards
