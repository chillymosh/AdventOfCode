open List

type cube_counts = { red: int; green: int; blue: int }
type game_data = { game_id: int; rounds: cube_counts list }

let parse_score score =
  let parts = String.split_on_char ' ' score in
  match parts with
  | [value; "red"] -> { red = int_of_string value; green = 0; blue = 0 }
  | [value; "green"] -> { red = 0; green = int_of_string value; blue = 0 }
  | [value; "blue"] -> { red = 0; green = 0; blue = int_of_string value }
  | _ -> failwith "Invalid score format"


let safe_int_of_string str =
  try int_of_string str with
  | Failure _ -> failwith ("Invalid number: " ^ str)


let parse_round round =
  let scores = String.split_on_char ',' round in
  fold_left (fun acc score ->
      let sc = parse_score (String.trim score) in
      { red = max acc.red sc.red; green = max acc.green sc.green; blue = max acc.blue sc.blue }
    ) { red = 0; green = 0; blue = 0 } scores


let parse_game game_str =
  match String.split_on_char ':' game_str with
  | [game_id_str; rounds_str] ->
    let parts = String.split_on_char ' ' (String.trim game_id_str) in
    (match parts with
     | _ :: id_str :: _ -> 
       let game_id = safe_int_of_string id_str in
       let rounds = String.split_on_char ';' (String.trim rounds_str) in
       let cube_counts = map (fun r -> parse_round (String.trim r)) rounds in
       Some { game_id; rounds = cube_counts }
     | _ -> failwith "Invalid game ID format")
  | _ -> failwith "Invalid game string format"


let is_game_possible cube_limits game =
  fold_left (fun acc round ->
      acc && round.red <= cube_limits.red && round.green <= cube_limits.green && round.blue <= cube_limits.blue
    ) true game.rounds

let total_power_of_sets games =
  fold_left (fun acc game ->
      let max_cubes = fold_left (fun acc round ->
          { red = max acc.red round.red;
            green = max acc.green round.green;
            blue = max acc.blue round.blue }) { red = 0; green = 0; blue = 0 } game.rounds in
      acc + max_cubes.red * max_cubes.green * max_cubes.blue) 0 games


let read_lines name : string list =
  let ic = open_in name in
  let try_read () =
    try Some (input_line ic) with End_of_file -> None in
  let rec loop acc = match try_read () with
    | Some s -> loop (s :: acc)
    | None -> close_in ic; rev acc in
  loop []


let main data cube_limits =
  let games = filter_map parse_game data in
  let possible_games = filter (is_game_possible cube_limits) games in
  let sum_of_ids = fold_left (fun acc game -> acc + game.game_id) 0 possible_games in
  let total_power = total_power_of_sets games in
  (sum_of_ids, total_power)


let () =
  if Array.length Sys.argv < 2 then
    Printf.eprintf "Usage: %s <filename>\n" Sys.argv.(0)
  else
    let filename = Sys.argv.(1) in
    let game_data = read_lines filename in
    let cube_limits = { red = 12; green = 13; blue = 14 } in
    let (sum_of_ids, sum_of_powers) = main game_data cube_limits in
    Printf.printf "Part 1 Total: %d\nPart 2 Total: %d\n" sum_of_ids sum_of_powers