let is_numeric str =
        String.length str > 0 && String.for_all (fun c -> c >= '0' && c <= '9') str
      
      
      let parse_numbers string =
        string
        |> String.split_on_char ' '
        |> List.filter is_numeric
        |> List.map int_of_string
      
      let get_score time dist = 
        let x = sqrt ((time *. time) /. 4. -. dist) in
        let lower = int_of_float (floor (time /. 2. -. x +. 1.)) in
        let upper = int_of_float (ceil (time /. 2. +. x -. 1.)) in
        upper - lower + 1
      
      
      let lines = Core.In_channel.input_lines stdin
      
      let times = List.map float_of_int (parse_numbers (List.nth (String.split_on_char ':' (List.nth lines 0)) 1))
      let dists = List.map float_of_int (parse_numbers (List.nth (String.split_on_char ':' (List.nth lines 1)) 1))
      
      let remove_spaces = Core.String.filter ~f:(fun (c) -> c != ' ')
      let fulltime = float_of_string (remove_spaces (List.nth (String.split_on_char ':' (List.nth lines 0)) 1))
      let fulldist = float_of_string (remove_spaces (List.nth (String.split_on_char ':' (List.nth lines 1)) 1))
      
      let scores = List.map2 get_score times dists
      
      let () = Printf.printf "%d\n" (List.fold_left ( * ) 1 scores)
      let () = Printf.printf "%d\n" (get_score fulltime fulldist)