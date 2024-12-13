import scala.collection.mutable.Set

@main def d12p1(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toArray

  val (rows, cols) = (lines.length, lines(0).length)
  var seen = Set[(Int, Int)]()

  // we can compose the semigroups to avoid redundant work!
  def dfs(r: Int, c: Int, id: Int): (Int, Int) =
    if r < 0 || c < 0 || r >= rows || c >= cols then (0, 1)
    else if lines(r)(c) != id then (0, 1)
    else if seen((r, c)) then (0, 0)
    else
      seen += ((r, c))
      Seq(
        dfs(r + 1, c, id),
        dfs(r, c + 1, id),
        dfs(r - 1, c, id),
        dfs(r, c - 1, id)
      ).fold((1, 0)) { (acc, cur) => (acc._1 + cur._1, acc._2 + cur._2) }

  println((for
    r <- 0 until rows
    c <- 0 until cols
  yield
    val (a, p) = dfs(r, c, lines(r)(c))
    a * p
  ).sum)
