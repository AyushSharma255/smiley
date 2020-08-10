let canvas
let eyeWidth
let eyeHeight
let happiness
let smileWidth

function setup() {
    canvas = createCanvas(500, 500)
    canvas.parent("canvas-container")

    eyeWidth = createSlider(5, 100)
    eyeWidth.parent("eye-width")

    eyeHeight = createSlider(5, 100)
    eyeHeight.parent("eye-height")

    happiness = createSlider(5, 325)
    happiness.parent("happiness")

    smileWidth = createSlider(5, 50, 5)
    smileWidth.parent("happy-width")
}

function draw() {
    smooth()
    background(255, 255, 255)
    fill(255)
    strokeWeight(5)
    ellipse(250, 250, 400)
    fill(0)
    ellipse(150, 200, eyeWidth.value(), eyeHeight.value())
    ellipse(350, 200, eyeWidth.value(), eyeHeight.value())
    fill(0, 0, 0, 0)
    bezier(
        150 - smileWidth.value(), 300,
        250, 300 + happiness.value(),
        350 + smileWidth.value(), 300, // function needs to have 4 args
        350 + smileWidth.value(), 300 // this is a clone arg
    )
}

setInterval(() => {
    if (canvas) {
        let _eyeWidth = document.querySelector("body > section > form > input[type=hidden]:nth-child(4)")
        let _eyeHeight = document.querySelector("body > section > form > input[type=hidden]:nth-child(5)")
        let _happiness = document.querySelector("body > section > form > input[type=hidden]:nth-child(6)")
        let _smileWidth = document.querySelector("body > section > form > input[type=hidden]:nth-child(7)")

        _eyeWidth.value = eyeWidth.value()
        _eyeHeight.value = eyeHeight.value()
        _happiness.value = happiness.value()
        _smileWidth.value = smileWidth.value()

        canvas.elt.style.width = "100%"
        canvas.elt.style.height = "100%"
    }
}, 1)