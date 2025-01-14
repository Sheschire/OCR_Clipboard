#Requires AutoHotkey v2.0

!`:: ;
{
    FolderPath := <your path of the project>

    RunWait("SnippingTool /clip")
    Sleep(500)

    PythonPath := <your path to python>
    RunWait(PythonPath . " " . FolderPath . "OCR_Clipboard.py")

    return
}
