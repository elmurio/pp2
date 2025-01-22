{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, World!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello, World!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "num = 54 ## integer\n",
    "numf = 5.4 ## float\n",
    "numb = True ## boolean\n",
    "numcx = 5 + 4j ## complex\n",
    "stringvar = \"string\" ## string variabe (can also be declared with ' ')\n",
    "\n",
    "num = int(54) #-------casting variables-------\n",
    "numf = float(5.4)\n",
    "numb = bool(1)\n",
    "numcx = complex(5+4j)\n",
    "stringvar = str(\"string\")\n",
    "\n",
    "#Variables dont need to be declared with specific type,unlike C++\n",
    "#Variables must start with alphabet symbol,and it cant contain any special symbols,except underscore ( _ )\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# each Python file has .py extension. However, we use .ipynb when it comes to handy notebooks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Indentation (Tabs) are a way to separate body parts from operators (if,else,elif,functions etc).\n",
    "# Unlike C++ spaces and indentation plays a crucial role in syntax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your number is less than 2\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Enter some number : \"))\n",
    "\n",
    "if x > 2:\n",
    "    print(\"Your number is greater 2\")\n",
    "elif x < 2:\n",
    "    print(\"Your number is less than 2\")\n",
    "else:\n",
    "    print(\"Your number is exactly 2\")\n",
    "\n",
    "#Base case for Conditional operations (if,elif,else). Here we can spot the difference between\n",
    "#C++ and Python Syntaxes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Python has useful data structures like\n",
    "# List,Set,Dict,Tuple\n",
    "lst = [1,2,3,'four',4,'three',2,True] #obvious container with some elements\n",
    "st = {'a','b','capybara'} #set with unique sorted values (all the repetitions get nullified)\n",
    "mp = {\"5\" : 2} #basically map from C++.List of pairs in {key,value} format.Each key is unique\n",
    "tple = ('wakeup','dosomebiz','gotosleep') #tuple - immutable list that cannot be changed in any way (order,amount of elements,etc.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#All the structures can be declared in many ways\n",
    "x = tuple((1,2,3))\n",
    "x = list(('a','b'))\n",
    "#and so on.To check the type of variable we can use type(variable)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Python has a few modules that we can import to use some features.Example with random module\n",
    "\n",
    "import random\n",
    "\n",
    "print(random.randrange(1, 10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "He is called 'Johnny'\n"
     ]
    }
   ],
   "source": [
    "print(\"He is called 'Johnny'\") #we can use quotes inside of quotes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#multiline string\n",
    "a = \"\"\"Lorem ipsum dolor sit amet, \n",
    "consectetur adipiscing elit,\n",
    "sed do eiusmod tempor incididunt\n",
    "ut labore et dolore magna aliqua.\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s\n",
      "t\n",
      "r\n",
      "i\n",
      "n\n",
      "g\n",
      "v\n",
      "r\n"
     ]
    }
   ],
   "source": [
    "#String members can be accesed via [] operator,as well as data structures\n",
    "\n",
    "stringvar[0]\n",
    "\n",
    "#we can also loop through strings\n",
    "for x in \"stringvar\":\n",
    "    if(x != 'a'):\n",
    "        print(x)\n",
    "\n",
    "\n",
    "#length of a string\n",
    "len(stringvar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "txt = \"The best things in life are free!\"\n",
    "print(\"free\" in txt)\n",
    "\n",
    "txt = \"The best things in life are free!\"\n",
    "print(\"free\" not in txt)\n",
    "\n",
    "#boolean logic in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "llo, World!\n",
      "orl\n"
     ]
    }
   ],
   "source": [
    "#Get the characters from the start to position 5 (not included):\n",
    "\n",
    "b = \"Hello, World!\"\n",
    "print(b[:5])\n",
    "\n",
    "\n",
    "#Get the characters from position 2, and all the way to the end:\n",
    "\n",
    "print(b[2:])\n",
    "\n",
    "#Get the characters:\n",
    "#From: \"o\" in \"World!\" (position -5)\n",
    "#To, but not included: \"d\" in \"World!\" (position -2):\n",
    "\n",
    "print(b[-5:-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO, WORLD!\n",
      "hello, world!\n",
      "Hello, World!\n",
      "Jello, World!\n",
      "['Hello', ' World!']\n"
     ]
    }
   ],
   "source": [
    "a = \"Hello, World!\"\n",
    "#The upper() method returns the string in upper case:\n",
    "print(a.upper())\n",
    "\n",
    "#The lower() method returns the string in lower case:\n",
    "print(a.lower())\n",
    "\n",
    "#The strip() method removes any whitespace from the beginning or the end:\n",
    "print(a.strip()) # returns \"Hello, World!\"\n",
    "\n",
    "\n",
    "#The replace() method replaces a string with another string:\n",
    "print(a.replace(\"H\", \"J\"))\n",
    "\n",
    "#Example\n",
    "#The split() method splits the string into substrings if it finds instances of the separator:\n",
    "print(a.split(\",\"))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Concatenation\n",
    "a = \"Hello\"\n",
    "b = \"World\"\n",
    "c = a + b\n",
    "print(c)\n",
    "\n",
    "# Create an f-string (formatting text,adding some variables)\n",
    "age = 36\n",
    "txt = f\"My name is John, I am {age}\"\n",
    "print(txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'We are the so-called \"Vikings\" from the north.'"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#The escape character ( \\ ) allows you to use double quotes when you normally would not be allowed:\n",
    "txt = \"We are the so-called \\\"Vikings\\\" from the north.\"\n",
    "print(txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Python has tons of built in methods that manipulate strings\n",
    "\n",
    "capitalize()\t#Converts the first character to upper case\n",
    "casefold()\t#Converts string into lower case\n",
    "center()\t#Returns a centered string\n",
    "count()\t#Returns the number of times a specified value occurs in a string\n",
    "encode()\t#Returns an encoded version of the string\n",
    "endswith()\t#Returns true if the string ends with the specified value\n",
    "expandtabs()\t#Sets the tab size of the string\n",
    "find()\t#Searches the string for a specified value and returns the position of where it was found\n",
    "format()\t#Formats specified values in a string\n",
    "format_map()\t#Formats specified values in a string\n",
    "index()\t#Searches the string for a specified value and returns the position of where it was found\n",
    "isalnum()\t#Returns True if all characters in the string are alphanumeric\n",
    "isalpha()\t#Returns True if all characters in the string are in the alphabet\n",
    "isascii()\t#Returns True if all characters in the string are ascii characters\n",
    "isdecimal()\t#Returns True if all characters in the string are decimals\n",
    "isdigit()\t#Returns True if all characters in the string are digits\n",
    "isidentifier()\t#Returns True if the string is an identifier\n",
    "islower()\t#Returns True if all characters in the string are lower case\n",
    "isnumeric()\t#Returns True if all characters in the string are numeric\n",
    "isprintable()\t#Returns True if all characters in the string are printable\n",
    "isspace()\t#Returns True if all characters in the string are whitespaces\n",
    "istitle()\t#Returns True if the string follows the rules of a title\n",
    "isupper()\t#Returns True if all characters in the string are upper case\n",
    "join()\t#Joins the elements of an iterable to the end of the string\n",
    "ljust()\t#Returns a left justified version of the string\n",
    "lower()\t#Converts a string into lower case\n",
    "lstrip()\t#Returns a left trim version of the string\n",
    "maketrans()\t#Returns a translation table to be used in translations\n",
    "partition()\t#Returns a tuple where the string is parted into three parts\n",
    "replace()\t#Returns a string where a specified value is replaced with a specified value\n",
    "rfind()\t#Searches the string for a specified value and returns the last position of where it was found\n",
    "rindex()\t#Searches the string for a specified value and returns the last position of where it was found\n",
    "rjust()\t#Returns a right justified version of the string\n",
    "rpartition()\t#Returns a tuple where the string is parted into three parts\n",
    "rsplit()\t#Splits the string at the specified separator, and returns a list\n",
    "rstrip()\t#Returns a right trim version of the string\n",
    "split()\t#Splits the string at the specified separator, and returns a list\n",
    "splitlines()\t#Splits the string at line breaks and returns a list\n",
    "startswith()\t#Returns true if the string starts with the specified value\n",
    "strip()\t#Returns a trimmed version of the string\n",
    "swapcase()\t#Swaps cases, lower case becomes upper case and vice versa\n",
    "title()\t#Converts the first character of each word to upper case\n",
    "translate()\t#Returns a translated string\n",
    "upper()\t#Converts a string into upper case\n",
    "zfill()\t#Fills the string with a specified number of 0 values at the beginning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}