from pyscript import document, display


def adding_numbers(e): #e for event handling
    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)
    result = (num1 + num2)//2

    #to show average
    display(result, target="output1")

    # Check if they pass/fail
    if result >= 75:
        display("Yes, you passed ✅😊", target="output2")
    else:
        display("No, you failed ❌😞", target="output2")