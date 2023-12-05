let is_numeric str =
  String.length str > 0 && String.for_all (fun c -> c >= '0' && c <= '9') str

let parse_numbers string =
  string
  |> String.split_on_char ' '
  |> List.filter is_numeric
  |> List.map int_of_string


let range_intersect (x,y) (a,b) = 
  let left = max x a in
  let right = min y b in
  (left, max left right)

let rec get_maps lines =
  let rec aux (acc : string list list) = function
    | [] -> List.rev acc
    | line::rest ->
      if String.trim line = "" then aux ([]::acc) rest
      else aux (((String.trim line)::(List.hd acc))::(List.tl acc)) rest
  in
  aux [[]] lines 
  |> List.filter (fun x -> x <> []) 
  |> List.map (fun x -> List.tl (List.rev x))
  |> List.map (List.map parse_numbers)

let range_map (x, y, z) (a, b) =
  let (left, right) = range_intersect (x, x + z) (a, b) in
  if left >= right then [(a, b)], []
  else ([(a, left); (right, b)] |> List.filter (fun (x, y) -> x < y), [(left + y - x, right + y - x)])

let parse_range_mapper line = (List.nth line 1, List.nth line 0, List.nth line 2)

let get_min_location seed_ranges maps =
  let seeds = ref seed_ranges in
  let () = List.iter (fun map -> 
      let rec aux lines remaining fin = match lines with
        | [] -> remaining @ fin
        | line::rest -> 
          let mapper = parse_range_mapper line in
          let ranges = List.map (range_map mapper) remaining in
          let (x, y) = List.fold_left (fun acc arr -> (fst acc @ fst arr, snd acc @ snd arr)) ([], []) ranges in
          aux rest x (fin @ y)
      in
      seeds := aux map !seeds []) maps in
  Option.get (Core.List.min_elt ~compare:Int.compare (List.map fst !seeds))

let get_seed_ranges1 seeds = List.map (fun a -> (a, a + 1)) seeds

let rec get_seed_ranges2 = function
  | [] -> []
  | x::y::rest -> (x, x + y - 1)::get_seed_ranges2 rest
  | _ -> failwith "invalid input"

let () =
  let argv = Sys.argv in
  if Array.length argv < 2 then (
    Printf.eprintf "Usage: %s <filename>\n" argv.(0);
    exit 1
  );
  let filename = argv.(1) in
  let input_lines = Core.In_channel.read_lines filename in
  let seeds = parse_numbers (List.nth (String.split_on_char ':' (List.hd input_lines)) 1) in
  let maps = get_maps (List.tl (List.tl input_lines)) in

  let part1_result = get_min_location (get_seed_ranges1 seeds) maps in
  Printf.printf "Part 1 Result: %d\n" part1_result;

  let part2_result = get_min_location (get_seed_ranges2 seeds) maps in
  Printf.printf "Part 2 Result: %d\n" part2_result;