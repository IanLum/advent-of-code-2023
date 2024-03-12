import java.io.File
import kotlin.math.abs

const val fileIdx = 0
// real = 0, test = 1
val files = listOf("day18", "day18_test")

data class Vector(val x: Int, val y: Int) {
    operator fun plus(v: Vector) = Vector(x + v.x, y + v.y)
    operator fun times(i: Int) = Vector(i*x, i*y)
}
fun part1(lines: List<String>): Int {
    var curr = Vector(0,0)
    val points = mutableListOf(Vector(0,0))

    val dirMap = mapOf(
        "U" to Vector(0, 1),
        "D" to Vector(0, -1),
        "R" to Vector(1, 0),
        "L" to Vector(-1, 0)
    )

    var perim = 0
    lines.forEach {
        val (dir, distStr) = it.split(" ")
        val dist = distStr.toInt()
        curr += dirMap[dir]!! * dist
        perim += dist
        points.add(curr)
    }
    var sum = 0
    points.dropLast(1).forEachIndexed { idx , pt ->
        sum += (pt.y + points[idx+1].y) * (pt.x - points[idx+1].x)
    }
    return abs(sum/2) + perim/2 + 1
}

fun main() {
    val lines = File("data/${files[fileIdx]}.txt").readLines()
    println(part1(lines))
}
