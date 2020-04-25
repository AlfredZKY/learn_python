# 使用原因  
    - 当我们在用requests抓取页面的时候，得到的结果可能会和在浏览器中看到的不一样：在浏览器中正常显示的页面数据，使用requests却没有得到结果。
    - 这是因为 requests 获取的都是原始 HTML 文档，而浏览器中的页面则是经过 JavaScript 数据处理后生成的结果
        - 1.数据加载是一种异步加载方式，原始页面不包含某些数据，只有在加载完成后，才向服务器请求某个接口获取数据，然后处理后显示在网页上，发送了Ajax请求
        - 2.经过JavaScript 和特定算法计算后生成的
        
# 等待条件
|  等待条件| 含义 |
| ------ |------|
| title_is | 标题某内容 |
| title_contains | 标题包含某内容 |
| presence_of_element_located | 节点加载出，传入定位元组，如（By.ID,'p'） |
| visibility_of_element_located | 节点可见，传入定位元组 |
| visibility_of | 可见，传入节点对象 |
| presence_of_all_elements_located | 所有节点加载出 |
| text_to_be_present_in_element | 某个节点文本包含某文字 |
| text_to_be_present_in_element_value | 某个节点值包含某文字 |
| frame_to_be_available_and_switch_to_itframe | 加载并切换 |
| invisibility_of_element_located | 节点不可见 |
| element_to_be_clickable | 节点可点击 |
| staleness_of | 判断一个节点是否仍在DOM，可判断页面是否已经刷新 |
| element_to_be_selected | 节点可选择，传节点对象 |
| element_located_to_be_selected | 节点可选择，传入定位元组 |
| element_selection_state_to_be | 传入节点对象以及状态，相等返回True,否则返回False |
| alert_is_present | 是否出现alert |
| invisibility_of_element_located | 节点不可见 |


