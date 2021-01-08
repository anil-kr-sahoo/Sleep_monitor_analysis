import PySimpleGUI as sg


def input_given(**kwargs):
    data_list = kwargs.get("data_list", None)
    date_required = kwargs.get("date_required", None)
    if data_list:
        if date_required:
            form = sg.FlexForm('Select Your Specific Date')
            start_index = 0
            layout = list()

            while True:
                if start_index >= len(data_list):
                    break
                else:
                    end_index = start_index + 10
                    if end_index >= len(data_list):
                        end_index = len(data_list)
                    layout.append([sg.Text(data_list[start_index: end_index])])
                    start_index += 10

            layout.append([sg.Text('')])
            layout.append([sg.Text('Select a Date', size=(15, 1)), sg.InputText('')])
            layout.append([sg.Submit(), sg.Cancel()])

            button, values = sg.Window.Layout(self=form, rows=layout).Read()
            if button == "Cancel":
                print('\nThankYou for Using our Software')
            else:
                sg.Window.Close(self=form)
                return values[0]
        else:
            form = sg.FlexForm('Select Your Specific Month')
            start_index = 0
            layout = list()
            while True:
                if start_index >= len(data_list):
                    break
                else:
                    end_index = start_index + 4
                    if end_index >= len(data_list):
                        end_index = len(data_list)
                    layout.append([sg.Text(data_list[start_index: end_index])])
                    start_index += 4

            layout.append([sg.Text('')])
            layout.append([sg.Text('Select a Month', size=(15, 1)), sg.InputText('')])
            layout.append([sg.Submit(), sg.Cancel()])

            button, values = sg.Window.Layout(self=form, rows=layout).Read()
            if button == "Cancel":
                print('\nThankYou for Using our Software')
            else:
                sg.Window.Close(self=form)
                return values[0]
    else:
        pass
