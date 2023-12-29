# assign selected editor info when team list clicked---------------------
def team_list_clicked(main):
    main.selected_indexes=[]
    main.selected_user_ids=[]
    main.selected_maproulette_ids=[]
    main.selected_editors=[]
    main.selected_editors=main.teamList.selectedItems()
    if not main.selected_editors ==None: 
        for i in main.selected_editors:
            j=main.teamList.indexOfTopLevelItem(i)
            main.selected_indexes.append(j)
            main.selected_maproulette_ids.append(i.text(3))
            main.selected_user_ids.append(i.text(2))
