module CharMap = Map.Make(Char)

let initialize_map mappings =
  List.fold_left (fun acc (k, v) -> CharMap.add k v acc) CharMap.empty mappings

let card_values = initialize_map [('2', 0); ('3', 1); ('4', 2); ('5', 3); ('6', 4);
                                  ('7', 5); ('8', 6); ('9', 7); ('T', 8); ('J', 9);
                                  ('Q', 10); ('K', 11); ('A', 12)]

let card_values2 = initialize_map [('J', 0); ('2', 1); ('3', 2); ('4', 3); ('5', 4);
                                   ('6', 5); ('7', 6); ('8', 7); ('9', 8); ('T', 9);
                                   ('Q', 10); ('K', 11); ('A', 12)]

let read_file filename =
  let lines = ref [] in
  let chan = open_in filename in
  try
    while true; do
      lines := input_line chan :: !lines
    done; !lines
  with End_of_file ->
    close_in chan;
    List.rev !lines

let parse_line line =
  match String.split_on_char ' ' line with
  | [hand; bid_str] -> (hand, int_of_string bid_str)
  | _ -> failwith "Invalid line format"

let count_cards str =
  String.fold_left (fun acc c ->
      let count = CharMap.find_opt c acc |> Option.value ~default:0 in
      CharMap.add c (count + 1) acc
    ) CharMap.empty str

let part1 hand =
  let counts = count_cards hand in
  let hand_type = CharMap.bindings counts |> List.map snd |> List.sort compare |> List.rev in
  (hand_type, String.to_seq hand |> List.of_seq |> List.map (fun c -> CharMap.find c card_values))

let part2 hand =
  let counts = count_cards hand in
  let jokers = CharMap.find_opt 'J' counts |> Option.value ~default:0 in
  let counts = CharMap.remove 'J' counts in
  let hand_type = CharMap.bindings counts |> List.map snd |> List.sort compare |> List.rev in
  let hand_type = match hand_type with
    | [] -> [jokers]
    | h :: t -> (h + jokers) :: t
  in
  (hand_type, String.to_seq hand |> List.of_seq |> List.map (fun c -> CharMap.find c card_values2))

let calculate_sum sorted_hands =
  let rec aux sum i = function
    | [] -> sum
    | (_, bid) :: t -> aux (sum + bid * (i + 1)) (i + 1) t
  in
  aux 0 0 sorted_hands

let () =
  if Array.length Sys.argv < 2 then
    (Printf.printf "Usage: %s <filename>\n" Sys.argv.(0); exit 1);
  let filename = Sys.argv.(1) in
  let lines = read_file filename in
  let hands_with_bids = List.map parse_line lines in
  let sorted_hands1 = List.sort (fun (hand1, _) (hand2, _) -> compare (part1 hand1) (part1 hand2)) hands_with_bids in
  let sorted_hands2 = List.sort (fun (hand1, _) (hand2, _) -> compare (part2 hand1) (part2 hand2)) hands_with_bids in
  let p1 = calculate_sum sorted_hands1 in
  let p2 = calculate_sum sorted_hands2 in
  Printf.printf "Total sum for part1: %d\n" p1;
  Printf.printf "Total sum for part2: %d\n" p2