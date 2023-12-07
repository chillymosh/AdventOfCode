module CharMap = Map.Make(Char)

let card_values = 
  List.fold_left (fun acc (k, v) -> CharMap.add k v acc) CharMap.empty 
    [('2', 0); ('3', 1); ('4', 2); ('5', 3); ('6', 4); ('7', 5); ('8', 6);
     ('9', 7); ('T', 8); ('J', 9); ('Q', 10); ('K', 11); ('A', 12)]

let card_values2 = 
  List.fold_left (fun acc (k, v) -> CharMap.add k v acc) CharMap.empty 
    [('J', 0); ('2', 1); ('3', 2); ('4', 3); ('5', 4); ('6', 5); ('7', 6);
     ('8', 7); ('9', 8); ('T', 9); ('Q', 10); ('K', 11); ('A', 12)]

let read_file filename =
  let chan = open_in filename in
  let rec read_lines acc =
    try
      let line = input_line chan in
      read_lines (line :: acc)
    with End_of_file -> acc
  in
  let lines = read_lines [] in
  close_in chan;
  List.rev lines

let parse_line line =
  match String.split_on_char ' ' line with
  | [hand; bid_str] -> (hand, int_of_string bid_str)
  | _ -> failwith "Invalid line format"

let count_cards str =
  String.fold_left (fun acc c ->
      CharMap.update c (function Some count -> Some (count + 1) | None -> Some 1) acc
    ) CharMap.empty str

let score include_jokers card_map hand =
  let counts = count_cards hand in
  let jokers = if include_jokers then CharMap.find_opt 'J' counts |> Option.value ~default:0 else 0 in
  let counts = if include_jokers then CharMap.remove 'J' counts else counts in
  let hand_type = CharMap.bindings counts |> List.map snd |> List.sort compare |> List.rev in
  let hand_type = if include_jokers then
    match hand_type with
    | [] -> [jokers]
    | h :: t -> (h + jokers) :: t
  else hand_type in
  let ranks = String.to_seq hand |> List.of_seq |> List.map (fun c -> CharMap.find c card_map) in
  (hand_type, ranks)

let part1 hand = score false card_values hand
let part2 hand = score true card_values2 hand

let calculate_sum sorted_hands =
  List.fold_left (fun (sum, i) (_, bid) -> (sum + bid * i, i + 1)) (0, 1) sorted_hands |> fst

let () =
  if Array.length Sys.argv < 2 then
    Printf.printf "Usage: %s <filename>\n" Sys.argv.(0)
  else
    let filename = Sys.argv.(1) in
    let lines = read_file filename in
    let p1 = calculate_sum (List.sort (fun (h1, _) (h2, _) -> compare (part1 h1) (part1 h2)) (List.map parse_line lines)) in
    let p2 = calculate_sum (List.sort (fun (h1, _) (h2, _) -> compare (part2 h1) (part2 h2)) (List.map parse_line lines)) in
    Printf.printf "Total sum for part1: %d\n Total sum for part2: %d\n" p1 p2;