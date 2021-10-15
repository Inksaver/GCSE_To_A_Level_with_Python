function main()	
	io.write("Type your name_") 	-- io.write() does NOT move to the next line
	name = io.read()				-- io.read() stores what you type when you press Enter
	
	print("Hello "..name)			-- the .. dots join (concatenate) words (strings) together
end

main()

print("Press Enter to quit")
io.read()