const wait = time => new Promise(resolve => setTimeout(resolve, time))

// GlitchedWriter: https://www.npmjs.com/package/glitched-writer


wait(2000)
	.then(() => glitchWrite(glitch_this, 'To TNP.API', ))
	.then(() => wait(2000))
	.then(() => glitchWrite(glitch_this, 'The owner of this is site is Thanapoom Somrak ;)))))))))))).'))
	.then(() => wait(2000))
	.then

	//.then(() => input.removeAttribute('disabled'))

const displayWriter = setGlitchedWriter(glitch_this)

input.addEventListener(
	'input',
	_.debounce(() => displayWriter.write(input.value), 500, {
		maxWait: 1000,
	}),
)

glitch_this.addEventListener(
	'glitchWrote',
	e => (logs.innerHTML += `<p>${e.detail.text}</p>`),
)
