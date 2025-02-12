import java.io.File
import kotlin.math.abs

const val fileIdx = 0
// real = 0, test = 1
val files = listOf("day18", "day18_test")

data class Vector(val x: Long, val y: Long) {
    operator fun plus(v: Vector) = Vector(x + v.x, y + v.y)
    operator fun times(i: Long) = Vector(i*x, i*y)
}

fun findArea(instructions: List<Pair<String, Long>>): Long {
    var curr = Vector(0,0)
    val points = mutableListOf(Vector(0,0))

    val dirMap = mapOf(
        "U" to Vector(0, 1),
        "D" to Vector(0, -1),
        "R" to Vector(1, 0),
        "L" to Vector(-1, 0)
    )

    var perim: Long = 0
    instructions.forEach {
//        println("${it.first}, ${it.second}")
        curr += dirMap[it.first]!! * it.second
        perim += it.second
        points.add(curr)
    }
    var sum: Long = 0
    points.dropLast(1).forEachIndexed { idx , pt ->
        sum += (pt.y + points[idx+1].y) * (pt.x - points[idx+1].x)
    }
    return abs(sum/2) + perim/2 + 1
}
fun part1(lines: List<String>): Long {
    val instructions = mutableListOf<Pair<String, Long>>()
    lines.forEach {
        val (dir, dist) = it.split(" ")
        instructions.add(Pair(dir, dist.toLong()))
    }
    return findArea(instructions)
}

fun part2(lines: List<String>): Long {
    val instructions = mutableListOf<Pair<String, Long>>()
    val numToDir = mapOf('0' to "R", '1' to "D", '2' to "L", '3' to "U")
    lines.forEach {
        val hex = it.split("#")[1]
        instructions.add(Pair(
            numToDir[hex[5]]!!,
            hex.take(5).toLong(radix = 16)
        ))
    }
    return findArea(instructions)
}

fun main() {
    val lines = File("data/${files[fileIdx]}.txt").readLines()
    println(part1(lines))
    println(part2(lines))
}
