
let read_lines name : string list =
  let ic = open_in name in
  let try_read () =
    try Some (input_line ic) with End_of_file -> None in
  let rec loop acc = match try_read () with
    | Some s -> loop (s :: acc)
    | None -> close_in ic; List.rev acc in
  loop []

  let is_digit c =
    c >= '0' && c <= '9'
  
  let get_number_from_string s start =
    let rec aux i =
      if i < String.length s && is_digit s.[i] then aux (i + 1)
      else String.sub s start (i - start) in
    aux start
  
  let adjacent_positions i j len =
    let positions = ref [] in
    for k = j - 1 to j + len do
      positions := (i - 1, k) :: !positions;
      positions := (i + 1, k) :: !positions;
    done;
    (!positions @ [(i, j - 1); (i, j + len)])
  
  let p1_a data =
    let ans = ref 0 in
    List.iteri (fun i line ->
      let rec find_numbers j =
        if j < String.length line then
          if is_digit line.[j] then
            let num = get_number_from_string line j in
            let len = String.length num in
            let positions = adjacent_positions i j len in
            let count = List.fold_left (fun acc (x, y) ->
              if x >= 0 && x < List.length data && y >= 0 && y < String.length (List.nth data x) && (List.nth data x).[y] <> '.' then acc + 1 else acc
            ) 0 positions in
            if count > 0 then ans := !ans + int_of_string num;
            find_numbers (j + len)
          else find_numbers (j + 1) in
      find_numbers 0
    ) data;
    !ans
  
  let p2_a data =
    let adj = Hashtbl.create 100 in
    List.iteri (fun i line ->
      let rec find_numbers j =
        if j < String.length line then
          if is_digit line.[j] then
            let num = get_number_from_string line j in
            let len = String.length num in
            let positions = adjacent_positions i j len in
            List.iter (fun (x, y) ->
              if x >= 0 && x < List.length data && y >= 0 && y < String.length (List.nth data x) && (List.nth data x).[y] <> '.' then
                let key = (x, y) in
                let current = try Hashtbl.find adj key with Not_found -> [] in
                Hashtbl.replace adj key (num :: current)
            ) positions;
            find_numbers (j + len)
          else find_numbers (j + 1) in
      find_numbers 0
    ) data;
    Hashtbl.fold (fun _ nums acc ->
      if List.length nums = 2 then acc + (int_of_string (List.nth nums 0)) * (int_of_string (List.nth nums 1)) else acc
    ) adj 0


let () =
  if Array.length Sys.argv < 2 then
    Printf.eprintf "Usage: %s <filename>\n" Sys.argv.(0)
  else
    let data = read_lines Sys.argv.(1) in
    print_endline (string_of_int (p1_a data));
    print_endline (string_of_int (p2_a data));
