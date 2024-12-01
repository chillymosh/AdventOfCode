let read_input file_path =
  let ic = open_in file_path in
  let rec parse acc_left acc_right =
    match input_line ic with
    | exception End_of_file -> close_in ic; (acc_left, acc_right)
    | line when String.trim line = "" -> parse acc_left acc_right 
    | line ->
      let parts = String.split_on_char ' ' line |> List.concat_map (String.split_on_char '\t') in
      match List.filter (fun s -> s <> "") parts with
      | [l; r] -> (try parse ((int_of_string l) :: acc_left) ((int_of_string r) :: acc_right) with Failure _ -> failwith ("Invalid number in line: " ^ line))
      | _ -> failwith ("Invalid line format: " ^ line)
  in
  parse [] []

let calculate_p1 left right =
  let sorted_left = List.sort compare left in
  let sorted_right = List.sort compare right in
  List.fold_left2 (fun acc l r -> acc + abs (l - r)) 0 sorted_left sorted_right

let calculate_p2 left right =
  let freq_table = List.fold_left (fun acc r ->
      let count = try Hashtbl.find acc r with Not_found -> 0 in
      Hashtbl.replace acc r (count + 1);
      acc
    ) (Hashtbl.create (List.length right)) right in
  List.fold_left (fun acc l -> acc + (l * (try Hashtbl.find freq_table l with Not_found -> 0))) 0 left

let () =
  let file_path = "../input.txt" in
  let left, right = read_input file_path in
  Printf.printf "%d\n" (calculate_p1 left right);
  Printf.printf "%d\n" (calculate_p2 left right)
