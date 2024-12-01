@main def main(full: Boolean = false): Unit =
 val input = full match {
   case false => scala.io.Source.fromFile("sample.in").getLines
   case true  => scala.io.Source.fromFile("d.in").getLines
 }

 println("")
