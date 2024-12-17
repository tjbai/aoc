import scala.collection.mutable

@main def d16p2(args: String*): Unit =
  enum Dir:
    case L, R, U, D

  val dirs = Dir.L :: Dir.R :: Dir.U :: Dir.D :: Nil

  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toArray

  val (rows, cols) = (lines.length, lines(0).length)
  val (dirL, dirR, dirU, dirD) = (0, 1, 2, 3)

  val (sr, sc) = (for
    r <- 0 until rows
    c <- 0 until cols
    if lines(r)(c) == 'S'
  yield (r, c))(0)

  val (er, ec) = (for
    r <- 0 until rows
    c <- 0 until cols
    if lines(r)(c) == 'E'
  yield (r, c))(0)

  implicit val ordering: Ordering[(Int, Int, Int, Dir, List[(Int, Int)])] = Ordering.by {
    case (p, r, c, d, ls) => -p
  }
  var pq = mutable.PriorityQueue((0, sr, sc, Dir.R, List((sr, sc))))
  var best = mutable.Map[(Int, Int, Dir), Int]().withDefaultValue(1e9.toInt)
  var paths = mutable.Map[Dir, Set[(Int, Int)]]().withDefaultValue(Set.empty)

  while pq.nonEmpty do
    val (p, r, c, d, ls) = pq.dequeue
    if lines(r)(c) != '#' && p <= best((r, c, d)) then
      if lines(r)(c) == 'E' && p < best((r, c, d)) then paths(d) = ls.toSet
      else if lines(r)(c) == 'E' && p == best((r, c, d)) then paths(d) ++= ls.toSet
      best((r, c, d)) = p
      for (dr, dc, nd) <- Seq((0, -1, Dir.L), (0, 1, Dir.R), (-1, 0, Dir.U), (1, 0, Dir.D))
      do pq += ((p + 1 + (if nd != d then 1000 else 0), r + dr, c + dc, nd, (r, c) :: ls))

  val bestEnd = dirs.map(d => best((er, ec, d))).min

  println(
    dirs
      .filter(d => best((er, ec, d)) == bestEnd)
      .map(d => paths(d))
      .flatten
      .toSet
      .size + 1
  )
