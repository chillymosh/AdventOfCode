let word_to_num = function
  | "zero" -> "0"
  | "one" -> "1"
  | "two" -> "2"
  | "three" -> "3"
  | "four" -> "4"
  | "five" -> "5"
  | "six" -> "6"
  | "seven" -> "7"
  | "eight" -> "8"
  | "nine" -> "9"
  | s -> s 

let extract_first_last_numeric line =
  let length = String.length line in
  let rec find_digit is_forward index =
    if index < 0 || index >= length then None
    else if Char.code (String.get line index) >= 48 && Char.code (String.get line index) <= 57 then
      Some (String.make 1 (String.get line index))
    else
      find_digit is_forward (if is_forward then index + 1 else index - 1)
  in
  match find_digit true 0, find_digit false (length - 1) with
  | Some first, Some last -> first ^ last
  | _ -> "00"

let rec replace_words_with_digits_rec line =
  let regex = Str.regexp "\\(zero\\|one\\|two\\|three\\|four\\|five\\|six\\|seven\\|eight\\|nine\\)" in
  try
    let start = Str.search_forward regex line 0 in
    let matched_word = Str.matched_group 1 line in
    let digit = word_to_num matched_word in
    let prefix = Str.string_before line start in
    let suffix = Str.string_after line (start + String.length matched_word) in
    let new_line = prefix ^ digit ^ suffix in
    replace_words_with_digits_rec new_line
  with Not_found -> line


let replace_extract line =
  let replaced_line = replace_words_with_digits_rec line in
  extract_first_last_numeric replaced_line


let process_file_part1 filename =
  let input_data = open_in filename in
  let rec loop sum =
    match input_line input_data with
    | line ->
      let num_val = extract_first_last_numeric line in
      let num = int_of_string num_val in
      loop (sum + num)
    | exception End_of_file ->
      close_in input_data;
      sum
  in
  loop 0

let process_file_part2 filename =
  let in_channel = open_in filename in
  let rec loop sum =
    match input_line in_channel with
    | line ->
      let concat_num = replace_extract line in
      let num = int_of_string concat_num in
      loop (sum + num)
    | exception End_of_file ->
      close_in in_channel;
      sum
  in
  loop 0


let () =
  if Array.length Sys.argv < 2 then
    Printf.eprintf "Usage: %s <filename>\n" Sys.argv.(0)
  else
    let filename = Sys.argv.(1) in
    let total_part1 = process_file_part1 filename in
    let total_part2 = process_file_part2 filename in
    Printf.printf "Part 1 Total: %d\nPart 2 Total: %d\n" total_part1 total_part2