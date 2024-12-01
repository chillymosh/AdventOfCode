let preprocess_line line =
  line
  |> String.split_on_char '\t'
  |> String.concat " "
  |> String.trim

let read_input file_path =
  let ic = open_in file_path in
  let rec parse acc_left acc_right =
    match input_line ic with
    | exception End_of_file -> close_in ic; (List.rev acc_left, List.rev acc_right)
    | line when String.trim line = "" -> parse acc_left acc_right 
    | line ->
      let parts =
        preprocess_line line
        |> String.split_on_char ' '
        |> List.filter (fun s -> s <> "") 
      in
      match parts with
      | [l; r] ->
        (try
           let l = int_of_string l in
           let r = int_of_string r in
           parse (l :: acc_left) (r :: acc_right)
         with Failure _ ->
           failwith ("Invalid number in line: " ^ line))
      | _ -> failwith ("Invalid line format: " ^ line)
  in
  parse [] []

let calculate_p1 left right =
  let sorted_left = List.sort compare left in
  let sorted_right = List.sort compare right in
  List.fold_left2 (fun acc l r -> acc + abs (l - r)) 0 sorted_left sorted_right

let calculate_p2 left right =
  let freq_table = Hashtbl.create (List.length right) in
  List.iter (fun r ->
      let count = try Hashtbl.find freq_table r with Not_found -> 0 in
      Hashtbl.replace freq_table r (count + 1)
    ) right;
  List.fold_left (fun acc l ->
      let count = try Hashtbl.find freq_table l with Not_found -> 0 in
      acc + (l * count)
    ) 0 left

let () =
  let file_path = "../input.txt" in
  let left, right = read_input file_path in
  let p1 = calculate_p1 left right in
  Printf.printf "p1: %d\n" p1;
  let p2 = calculate_p2 left right in
  Printf.printf "p2: %d\n" p2
