@main def d7p1(args: String*): Unit =

  def concat(a: Long, b: Long): Long =
    (a * math.pow(10, math.floor(math.log10(b.toDouble)) + 1) + b).toLong

  def solve(targ: Long, arr: Array[Long], idx: Int = 0, acc: Long = 0): Boolean =
    if acc > targ then false
    else if idx == arr.length then acc == targ
    else
      solve(targ, arr, idx + 1, acc + arr(idx)) ||
      solve(targ, arr, idx + 1, acc * arr(idx)) ||
      solve(targ, arr, idx + 1, concat(acc, arr(idx)))

  println(
    scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .getLines
      .map(_.split(":"))
      .map(x => (x(0).toLong, x(1).split(" ").drop(1).map(_.toLong)))
      .filter(x => solve(x(0), x(1)))
      .map(_(0))
      .sum
  )
