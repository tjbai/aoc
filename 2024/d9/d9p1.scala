import scala.collection.mutable.ArrayBuffer

@main def d9p1(args: String*): Unit =
  val fs = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .next
    .map(x => (x - '0'))

  val res = ArrayBuffer[Long]()
  fs.zipWithIndex.foreach((x, i) =>
    if i % 2 == 0 then res ++= ArrayBuffer.fill(x)(i / 2)
    else res ++= ArrayBuffer.fill(x)(-1)
  )

  var l = res.indexOf(-1)
  while l > 0 && l < res.length do
    while l < res.length && res(l) != -1 do l += 1
    if l < res.length then
      res(l) = res(res.length - 1)
      res.remove(res.length - 1)

  println(res.zipWithIndex.view.map(_ * _).sum)
