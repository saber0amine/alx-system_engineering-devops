# A simple Ruby program

# Prompt the user for their name
print "Enter your name: "
user_name = gets.chomp

# Greet the user
puts "Hello, #{user_name}!"

# Calculate and display the length of the user's name
name_length = user_name.length
puts "The length of your name is: #{name_length} characters."

# Check if the name is longer than 10 characters
if name_length > 10
  puts "Wow, that's a long name!"
else
  puts "Nice and concise name!"
end

# Define a function to print a custom message
def custom_message(message)
  puts "Custom Message: #{message}"
end

# Call the function with a sample message
custom_message("Thanks for trying out this Ruby program!")

# End of the program
