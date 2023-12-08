let read_file filename =
  let ic = open_in filename in
  let try_read () =
    try Some (input_line ic) with End_of_file -> None in
  let rec loop acc = match try_read () with
    | Some s -> loop (s :: acc)
    | None -> close_in ic; List.rev acc in
  loop []

let rec gcd a b = if b = 0 then a else gcd b (a mod b)
let lcm a b = a * b / (gcd a b)

let create_paths lines =
  let paths_table = Hashtbl.create 1024 in  (* Adjust size based on expected number of paths *)
  let parse_line line =
    try
      let parts = Str.split (Str.regexp "[=(), ]+") line in
      match parts with
      | key :: left :: right :: _ -> Some (key, [("L", left); ("R", right)])
      | _ -> None
    with Not_found -> None
  in
  List.iter (fun line ->
    match parse_line line with
    | Some (key, value) -> Hashtbl.add paths_table key value
    | None -> ()
  ) lines;
  paths_table

let rec part1 paths pos dirs solution =
  if pos = "ZZZ" then solution
  else
    let dir_index = solution mod Array.length dirs in
    let dir = Array.get dirs dir_index in
    let new_pos = Hashtbl.find paths pos in
    let next_pos = List.assoc dir new_pos in
    part1 paths next_pos dirs (solution + 1)

let part2 paths dirs =
  let keys = Hashtbl.fold (fun key _ acc -> key :: acc) paths [] in
  let filtered_keys = List.filter (fun k -> String.get k 2 = 'A') keys in
  let rec helper pos i =
    if String.get pos 2 = 'Z' then i
    else
      let dir_index = i mod Array.length dirs in
      let dir = Array.get dirs dir_index in
      let new_pos = Hashtbl.find paths pos in
      let next_pos = List.assoc dir new_pos in
      helper next_pos (i + 1)
  in
  let is = List.map (fun k -> helper k 0) filtered_keys in
  List.fold_left lcm 1 is


let () =
  let filename = Sys.argv.(1) in
  let input = read_file filename in
  let dirs_str = List.hd input in 
  let dirs = Array.of_list (List.init (String.length dirs_str) (fun i -> String.make 1 dirs_str.[i])) in
  let paths = create_paths (List.tl input) in
  Printf.printf "%d\n" (part1 paths "AAA" dirs 0);
  Printf.printf "%d\n" (part2 paths dirs);