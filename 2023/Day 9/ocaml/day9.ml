let rec differences = function
  | a :: (b :: _ as t) -> (b - a) :: differences t
  | _ -> []

let rec build_sequences seq =
  seq :: (if List.for_all ((=) 0) seq then [] else build_sequences (differences seq))

let solve seq =
  List.fold_left (fun acc seq -> List.hd (List.rev seq) + acc) 0 (build_sequences seq)

let solve_from_file filename =
  let ic = open_in filename in
  let rec read_lines () =
    match input_line ic with
    | line -> (List.map int_of_string (String.split_on_char ' ' line)) :: read_lines ()
    | exception End_of_file -> []
  in
  let histories = read_lines () in
  close_in ic;
  (List.fold_left (fun acc seq -> acc + solve seq) 0 histories,
   List.fold_left (fun acc seq -> acc + solve (List.rev seq)) 0 histories)

let () =
  let p1, p2 = solve_from_file "input.txt" in
  Printf.printf "Part One Result: %d\nPart Two Result: %d\n" p1 p2