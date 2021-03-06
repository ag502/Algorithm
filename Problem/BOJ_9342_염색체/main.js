const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().trim().split("\n")
const [numOfChromosomes, ...chromosomes] = input

function checkPatterns (chromosome) {
    const pattern = /^[A-F]?A+F+C+[A-F]?$/
    const result = chromosome.match(pattern)

    if (result) {
        console.log('Infected!')
    } else {
        console.log('Good')
    }
}

chromosomes.forEach(chromosome => {
    checkPatterns(chromosome)
})

