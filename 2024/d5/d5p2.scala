import scala.collection.mutable.Queue
import scala.collection.mutable.Map

@main def d5p2(args: String*): Unit =
  val f = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .mkString

  val Array(rules, updates) = f.split("\n\n")

  val graph = rules
    .split("\n")
    .map(_.split("\\|"))
    .map(x => (x(0), x(1)))
    .groupBy(_(0))
    .mapValues(_.map(_(1)))
    .toMap
    .withDefaultValue(Array[String]())

  def isValid(update: Seq[String]): Boolean =
    var cache = Map[(String, String), Boolean]()
    var subgraph = graph.mapValues(_.filter(update.contains))
    def findChild(cur: String, dest: String): Boolean =
      cache.getOrElseUpdate(
        (cur, dest),
        if cur == dest then true
        else subgraph.getOrElse(cur, Array[String]()).exists(findChild(_, dest))
      )

    (for
      i <- 0 until update.length - 1
      j <- i + 1 until update.length
    yield !findChild(update(j), update(i))).reduce(_ & _)

  def getMiddle(update: Seq[String]): Int = update(update.length / 2).toInt

  def countIndegree(update: Array[String]): Map[String, Int] =
    val ind = Map[String, Int]().withDefaultValue(0)
    for (k, v) <- graph if update.contains(k) do v.foreach(x => ind(x) += 1)
    ind

  def reorder(update: Array[String]): List[String] =
    val ind = countIndegree(update)
    val q = update.filter(ind(_) == 0).to(Queue)
    var res = List[String]()
    while q.size > 0 do
      val cur = q.dequeue
      res = cur :: res
      graph(cur)
        .filter(update.contains(_))
        .foreach(child =>
          ind(child) -= 1
          if ind(child) == 0 then q.enqueue(child)
        )
    res.reverse

  println(
    updates
      .split("\n")
      .map(_.split(","))
      .withFilter(!isValid(_))
      .map(reorder)
      .map(getMiddle)
      .sum
  )
