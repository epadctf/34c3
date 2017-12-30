# m0rph
The easiest reversing challenge in 34c3CTF consisted of a jump table to functions XOR'ed with some byte.

We started out looking a looking on the binary statically, but soon turned to debugging in gdb inspecting the mmap'ed area. The binary constructs a jump table, and loaded what looked like code into the mmap'ed area. Since the mmap'ed area was readable, writeable and executeable we had strong indications that it was in fact code. We then dissasembled the code and found the first function in the jump table.

#### Manual mode
Later in the binary there were 2 'call rax', which we simply breakpointed and discovered it jumped into the functions we found where a comparison is made on the input argument. 
Each functions XOR's the next function and we decide to just continue on reading all of the compares manually whilst modifying our input in memory during debugging.

#### Automation (Post CTF)
After the CTF, we decided to write up a script to automate the behaviour we did manually. Check it out!
