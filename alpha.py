print([chr(a) for a in range(65,65+26) if chr(a) !=  [x.capitalize() for x in 'aeiou' ]  ] )
print([chr(a) for a in range(65,65+26) if chr(a) not in  [x.capitalize() for x in 'aeiou' ]  ] )
print([chr(a) for a in range(65,65+26) if chr(a)  in  [x.capitalize() for x in 'aeiou' ]  ] )

