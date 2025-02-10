let computer = "rock"
let player= "paper"
let results = computer === player
? "Tie game!"
: player === "rock" && computer === "paper"
? `player: ${player}\nComputer: ${computer}\nComputer wins!`
: player === "paper" && computer === "scissors"
? `player: ${player}\nComputer: ${computer}\nComputer wins!`
: player === "scissors" && computer === "rock"
? `player: ${player}\nComputer: ${computer}\nComputer wins!`
: `player: ${player}\nComputer: ${computer}\nplayer wins!`
console.log(results)