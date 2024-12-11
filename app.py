from  flask  import  Flask

app =  Flask( name )

@app.route('/')

def  hello_world( ) :

  return 'Akinggroup'

if  _name_ == "_main_" :

  app.run( )
