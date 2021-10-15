function input(prompt)
	io.write(prompt .. "_") 		-- "_" is added to prompt eg "Type your name_"
	return io.read()				-- io.read() sends what you typed in to where it was called
end

function main()
	name = input("Type your name")	
	age = input("Type your age")
	
	print("Hello " .. name)
	print("You are ".. age .. " years old")
end

main()
input("Press Enter to quit") -- this is now using the new input() function