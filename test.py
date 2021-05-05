import post_lib

if __name__=="__main__":
    server = post_lib.Server(host="127.0.0.1",port=5000,debug=True)
    server.run()