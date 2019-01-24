(* Prva naloga *)

let podvoji_vsoto a b = a + a + b + b

let povsod_vecji t1 t2 =
  match (t1, t2) with
  | ((a1, b1, c1), (a2, b2, c2)) when a1 > a2 && b1 > b2 && c1 > c2 -> true
  | ((_, _, _), (_, _, _)) -> false

let uporabi_ce_lahko f = function
  | Some x -> Some (f x)
  | None -> None

let pojavi_dvakrat x xs =
  let rec podvojitev acc n = function
  | [] -> (
    match acc with
    | 2 -> true
    | _ -> false
  )
  | x :: xs when x = n -> podvojitev (acc + 1) n xs
  | _ :: xs -> podvojitev acc n xs
  in
  podvojitev 0 x xs

let izracunaj_v_tocki t lst =
  let rec izracunaj acc t = function
  | [] -> acc
  | f :: fs -> izracunaj ((f t) :: acc) t fs
  in
  izracunaj [] t lst

let eksponent x p =
  let rec eksp acc n = function
  | 0 -> acc
  | s -> eksp (acc * n) n (s - 1)
  in eksp 1 x p


(* Druga naloga *)

type 'a mm_drevo = 
  | Empty
  | Node of 'a mm_drevo * 'a * int * 'a mm_drevo

let rec vstavi tree e =
  match tree with
  | Empty -> Node(Empty, e, 1, Empty)
  | Node(l, x, n, r) when e = x -> Node(l, x, (n+1), r)
  | Node(l, x, n, r) when e < x -> Node((vstavi l e), x, n, r)
  | Node(l, x, n, r) (* when e > x *) -> Node(l, x, n, (vstavi r e))

let multimnozica_iz_seznama lst =
  let rec sestavi acc = function
  | [] -> acc
  | x :: xs -> sestavi (vstavi acc x) xs
  in
  sestavi Empty lst

let rec velikost_multimnozice = function
  | Empty -> 0
  | Node(l, x, n, r) -> velikost_multimnozice l + n + velikost_multimnozice r

(* let rec seznam_iz_multimnozice tree =
  let rec veckratni_seznam acc y = function
    | 0 -> acc
    | p -> veckratni_seznam (y :: acc) y (p-1)
  in
  match tree with
  | Empty -> []
  | Node(l, x, n, r) -> (seznam_iz_multimnozice l) :: (veckratni_seznam [] x n) :: (seznam_iz_multimnozice r) *)

let seznam_iz_multimnozice tree =
  let rec veckratni_seznam acc y = function
    | 0 -> acc
    | p -> veckratni_seznam (y :: acc) y (p-1)
  in
  let aux lacc tacc = function
    | Empty -> 
      match tacc with
      | [] -> lacc
      | x :: xs -> aux lacc xs x
    | Node(l, x, n, r) -> aux lacc (Node(l, x, n, Empty) :: tacc) r
    | Node(l, x, n, Empty) -> aux laxx (Node(Empty, x, n, Empty) :: tacc) l
    | Node(Empty, x, n, Empty) -> aux ((veckratni_seznam [] x n) :: lacc) tacc Empty
    in
    aux [] [] tree


(* Tretja naloga - v loceni Python datoteki*)


let test1a = podvoji_vsoto 2 3

let test1b = povsod_vecji (2, 3, 4) (1, 2, 3) && povsod_vecji (2, 3, 4) (1, 2, 5)

let test1c = uporabi_ce_lahko ((+) 1) (Some 1)

let test1d = pojavi_dvakrat 1 [1; 1]

let test1e = izracunaj_v_tocki 1 [((+) 1); ((+) 2)]

let test1f = eksponent 2 3 + eksponent 1 1000000

let test2a = Node(Empty, 5, 2, Empty)

let test2b = vstavi test2a 3

let test2c = multimnozica_iz_seznama [2; 5; 1; 4; 1; 1; 2; 8; 8]

let test2d = velikost_multimnozice test2c

let test2e = seznam_iz_multimnozice test2c
