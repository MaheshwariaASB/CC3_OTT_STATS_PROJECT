- [ ] Finish pagination capabilities [1]

# [1]:

Separate query and write to file. By having query prepare one big JSON before sending to write, pagination issues could
be solved. Check for **hasMore** field in original response first, then find the nextCursor. Put all in JSON object,
inside of **shows**. Could be changed to just plain JSON but then _[dataManger.py]_ will need to be updated