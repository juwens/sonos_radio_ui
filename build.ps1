$env:INCLUDE = 'C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Tools\MSVC\14.30.30705\ATLMFC\include;C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Tools\MSVC\14.30.30705\include;C:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um;C:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\ucrt;C:\Program Files (x86)\Windows Kits\10\\include\10.0.19041.0\\shared;C:\Program Files (x86)\Windows Kits\10\\include\10.0.19041.0\\um;C:\Program Files (x86)\Windows Kits\10\\include\10.0.19041.0\\winrt;C:\Program Files (x86)\Windows Kits\10\\include\10.0.19041.0\\cppwinrt'

$env:LIB = 'C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Tools\MSVC\14.30.30705\ATLMFC\lib\x86;C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Tools\MSVC\14.30.30705\lib\x86;C:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\lib\um\x86;C:\Program Files (x86)\Windows Kits\10\lib\10.0.19041.0\ucrt\x86;C:\Program Files (x86)\Windows Kits\10\\lib\10.0.19041.0\\um\x86'

$cl = "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Tools\MSVC\14.29.30133\bin\Hostx86\x86\cl.exe"
& $cl "sonos_radio_launcher.cpp"