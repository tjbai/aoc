@main def d6p2(args: String*): Unit =
  val map = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toSeq

  // IDEA -- check all locations and keep a set of (r, c, d)
  // if we repeat then succ

  val (rows, cols) = (map.length, map(0).length)
  val dirs = IArray((-1, 0), (0, 1), (1, 0), (0, -1))

  def test(
      pos: (Int, Int),
      obs: (Int, Int),
      d: Int = 0,
      seen: Set[(Int, Int, Int)] = Set()
  ): Boolean =
    val (r, c) = pos
    if (seen.contains((r, c, d))) then true
    else
      val (nr, nc) = (r + dirs(d)(0), c + dirs(d)(1))
      (nr, nc) match
        case _ if (nr < 0 || nc < 0 || nr >= rows || nc >= cols) => false
        case _ if map(nr)(nc) == '#' || (nr, nc) == obs =>
          test(pos, obs, (d + 1) % 4, seen + ((r, c, d)))
        case _ => test((nr, nc), obs, d, seen + ((r, c, d)))

  val start = (for
    r <- 0 until rows
    c <- 0 until cols
    if map(r)(c) == '^'
  yield (r, c))(0)

  var res = 0
  for r <- 0 until rows do
    print(s"\r${"#" * r}${"." * (rows - r)}")
    System.out.flush()
    for
      c <- 0 until cols
      if (r, c) != start && map(r)(c) != '#'
    do if test(start, (r, c)) then res += 1

  println(res)
