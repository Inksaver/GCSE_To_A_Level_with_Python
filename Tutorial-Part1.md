<h1>Tutorial Part 1</h1>

The first code written in a text based language is the obligatory "Hello World"

such as [this one](/Lua/01-Hello%20World1.lua)
It is basically:
`print("Hello World")`
There is no reason why you should not start your coding experience using procedural techniques, right from the start, whatever the age group.

In a primary school setting
I go straight [to this](/Lua/02-Hello%20World2.lua)
```lua
function main()
	print("Hello World Version2")
end

main() -- 'Call' function called 'main()'

print("Press Enter to quit")
io.read()
```
So right from the start, students are using functions and procedures.
With a bit of practice printing out various lines of text to the console/IDE the desire for getting some input is requested. Lua does not have an input() function like Python, so you have to make your own.
This is how you can get [input from Lua:](/Lua/03-Input.lua)
```lua
function main()	
	io.write("Type your name_") 	-- io.write() does NOT move to the next line
	name = io.read()		-- io.read() stores what you type when you press Enter
	print("Hello "..name)		-- the .. dots join words (strings) together
end

main()
print("Press Enter to quit")
io.read()
```
The next logical step is to make an [input function:](/Lua/04-InputWithFunction.lua)
```lua
function input(prompt)
	io.write(prompt .. "_") -- "_" is added to prompt eg "Type your name_"
	return io.read()	-- io.read() sends what you typed in to where it was called
end

function main()
	name = input("Type your name")	
	age = input("Type your age")
	
	print("Hello " .. name)
	print("You are ".. age .. " years old")
end

main()
input("Press Enter to quit") -- this is now using the new input() function
```

This part demonstrated how the use of procedural programming can be used from the start, even in primary education.
Part 2 will move on to looking at Python scripts and how they can be improved in secondary education using the same techniques.

