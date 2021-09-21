#!/bin/bash

print_return_value () {
    if test $1 -eq 0; then
        echo -e "\n  ✅ \e[32m\e[1mDONE\e[0m"
    else
        echo -e "\n  ❌ \e[31m\e[1mFAILED\e[0m"
        exit 1
    fi
}

print_title () {
    echo -e "\n\e[32m\e[1m*** $1 ***\e[0m"
}

version="$(cat doc_version.txt)"

print_title "Generating output folder"
mkdir -p output
print_return_value $?

print_title "Building html"
make html
print_return_value $?

print_title "Zip HTML ouput"
cd build/html/
zip -r "html_output.zip" *
print_return_value $?

print_title "Move zip HTML ouput"
cd ../..
mv "build/html/html_output.zip" "./Robot-Coral-docs-$version.zip"
print_return_value $?

print_title "Building pdf"
make latexpdf
print_return_value $?

print_title "Moving pdf"
mv "build/latex/robotcoral.pdf" "./Robot-Coral-docs-$version.pdf"
print_return_value $?
