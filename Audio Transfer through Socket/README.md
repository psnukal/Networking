# Audio-Transfer-through-Socket
Audio file (.wav files) are transferred through sockets using TCP protocol

The "client_tcp" file should be run on the Client machine and "server_tcp" file should be run on the server machine with the audio file (.wav extension) present on the server machine in the same directory as that of the "server_tcp" code. If there is only one system present, both the "client_tcp" and "server_tcp" file can be run on the same system in different command prompt windows.

Audio files in .wav format is sent from server to client, where the client receives the 
audio stream. Transmission is lossless, uncompressed, 
quality retained and fast.

Libraries used :
socket - module that provides socket interface and API
PyAudio - a cross-platform audio i/o library, is used for python bindings.
wave - manages files of .wav audio formats
pickle - serializing and de-serializing python objects
struct - handles binary data in network connections

Data is serialized into binary, transmitted securely from server to client over a TCP 
connection. The client receives the serialized data, unserializes it and the audio data is
played instantly.

Note: Remember to change the Client's and Server's IP address to the appropriate address in the given code. The Audio file used here is just a test file. Any other audio file (with .wav extension) can also be used.

