


def team_list_clicked(main):
    main.selected_editors=main.teamList.selectedItems()
    main.selected_indexes=[]
    main.selected_user_ids=[]
    for i in main.selected_editors:
        j=main.teamList.indexOfTopLevelItem(i)
        main.selected_indexes.append(j)
        main.selected_user_ids.append(i.text(2))
  
    # root = main.teamList.invisibleRootItem()
    # child_count = root.childCount()
    # for i in range(child_count):
    #     item = root.child(i)
    #     item.setSelected(False)
    #     if main.teamList.indexOfTopLevelItem(item) in selectedIndexes:
    #         item.setSelected(True)      