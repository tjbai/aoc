@main def d5p1(args: String*): Unit =
  val f = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .mkString

  val Array(rules, updates) = f.split("\n\n")

  val graph = rules
    .split("\n")
    .map(_.split("\\|"))
    .map(x => (x(0), x(1)))
    .groupBy(_(0))
    .mapValues(x => x.map(_(1)))
    .toMap
    .withDefaultValue(Array[String]())

  def isValid(update: Seq[String]): Boolean =
    var cache = Map[(String, String), Boolean]()
    def findChild(cur: String, dest: String): Boolean =
      if cur == dest then true
      else if cache.contains((cur, dest)) then cache((cur, dest))
      else
        graph(cur)
          .filter(update.contains(_))
          .exists(child =>
            val exists = findChild(child, dest)
            cache = cache + ((cur, dest) -> exists)
            exists
          )

    (for
      i <- 0 until update.length - 1
      j <- i + 1 until update.length
    yield !findChild(update(j), update(i))).fold(true)(_ & _)

  def getMiddle(update: Array[String]): Int = update(update.length / 2).toInt

  println(
    updates
      .split("\n")
      .map(_.split(","))
      .filter(isValid)
      .map(getMiddle)
      .sum
  )
