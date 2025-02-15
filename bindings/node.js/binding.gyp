{
  "targets": [
    {
      "target_name": "kzg",
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "xcode_settings": {
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "13.0"
      },
      "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
      "sources": ["kzg.cxx"],
      "include_dirs": [
        "../../inc",
        "../../src",
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "libraries": [
        "<(module_root_dir)/c_kzg_4844.o",
        "<(module_root_dir)/../../lib/libblst.a"
      ],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": ["kzg"],
      "copies": [
        {
          "files": ["./build/Release/kzg.node"],
          "destination": "."
        }
      ]
    }
  ]
}
