import scala.collection.mutable.ArrayBuffer
import scala.util.boundary, boundary.break

@main def d9p2(args: String*): Unit =
  val fs = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .next
    .map(x => (x - '0').toInt)

  case class Block(sz: Int, offset: Int, id: Int = -1)
  val usedBlocks = ArrayBuffer[Block]()
  val emptyBlocks = ArrayBuffer[Block]()
  var offset = 0
  fs.zipWithIndex.foreach((sz, i) =>
    if i % 2 == 0 then usedBlocks += Block(sz, offset, i / 2)
    else emptyBlocks += Block(sz, offset)
    offset += sz
  )

  for (used, r) <- usedBlocks.zipWithIndex.reverse do
    boundary {
      for (empty, l) <- emptyBlocks.zipWithIndex if empty.offset < used.offset
      do
        if used.sz <= empty.sz then
          emptyBlocks(l) = empty.copy(sz = empty.sz - used.sz, offset = empty.offset + used.sz)
          usedBlocks(r) = used.copy(offset = empty.offset)
          break()
    }

  println(
    usedBlocks
      .map(b => (2 * b.offset + b.sz - 1) * ((b.sz) / 2.toDouble) * b.id)
      .sum
  )

  // r

  // println(data.view.map(_._1).sum)
