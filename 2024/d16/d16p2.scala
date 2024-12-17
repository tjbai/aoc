import scala.collection.mutable

@main def d16p2(args: String*): Unit =
  enum Dir:
    case L, R, U, D

  implicit val ordering: Ordering[(Int, Int, Int, Dir, List[(Int, Int)])] = Ordering.by {
    case (p, _, _, _, _) => -p
  }

  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toArray

  val (rows, cols) = (lines.length, lines(0).length)
  val sr = lines.indexWhere(_.contains('S'))
  val sc = lines(sr).indexOf('S')
  val er = lines.indexWhere(_.contains('E'))
  val ec = lines(er).indexOf('E')

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

  val bestEnd = Dir.values.map(d => best((er, ec, d))).min

  println(
    Dir.values
      .filter(d => best((er, ec, d)) == bestEnd)
      .flatMap(paths)
      .distinct
      .size + 1
  )
