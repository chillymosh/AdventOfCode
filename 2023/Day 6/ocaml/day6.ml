let calculate_ways_to_win time distance =
  let time = float_of_int time in
  let distance = float_of_int distance in
  let sqrt_part = sqrt ((time *. time) /. 4. -. distance) in
  let lower_bound = ceil (time /. 2. -. sqrt_part) in
  let upper_bound = floor (time /. 2. +. sqrt_part) in
  if upper_bound < lower_bound then 0 else int_of_float (upper_bound -. lower_bound) + 1

let read_file filename =
  let ic = open_in filename in
  let line1 = input_line ic in
  let line2 = input_line ic in
  close_in ic;
  (line1, line2)

let parse_line line =
  line
  |> String.split_on_char ' '
  |> List.filter (fun s -> s <> "")

let () =
  if Array.length Sys.argv < 2 then
    (Printf.printf "Usage: %s <filename>\n" Sys.argv.(0); exit 1);
  let filename = Sys.argv.(1) in
  let (time_line, distance_line) = read_file filename in
  let times = parse_line (String.sub time_line 5 (String.length time_line - 5)) in
  let distances = parse_line (String.sub distance_line 10 (String.length distance_line - 10)) in

  let p1 = List.fold_left2 (fun acc t d -> acc * calculate_ways_to_win (int_of_string t) (int_of_string d)) 1 times distances in

  let concatenated_time = int_of_string (String.concat "" times) in
  let concatenated_distance = int_of_string (String.concat "" distances) in

  let p2 = calculate_ways_to_win concatenated_time concatenated_distance in

  Printf.printf "Part 1 Result: %d\n" p1;
  Printf.printf "Part 2 Result: %d\n" p2;