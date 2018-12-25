/**分页js函数,forpage.js,此代码需要链接在html页面底部，同时需要先加载jquery框架**/

// li jquery object array
var newsLis = $("#news-lis").children();

// 新闻总数
var count = newsLis.length;

// 一页中最多显示的新闻数
var ONE_PAGE_COUNT = 5;

// 总页数
var totalPage = parseInt(count / ONE_PAGE_COUNT) + ((count % ONE_PAGE_COUNT) == 0? 0 : 1);

// 初始化页面
var currPage = 1;

// 用于设置新闻计数的函数
function setUICount(count) {
    if (count == undefined)
        count = 0;
    $("#cp-count").text(count);
}

//函数用于设置总的页面
function setUIPages(totalPage) {
    totalPage = Math.max(1, totalPage);
    $("#total-page").text(totalPage)
}

// 更新页面咕咕叫
function setUICurrPage(currPage) {
    currPage = Math.max(1, currPage);
    $("#curr-page").text(currPage);
}

// 传入显示的page参数，显示对应页面的新闻列表，隐藏其他列表
function scanAllForShow(page) {
    // page at least 1 or max totalPage
    page = Math.max(1, Math.min(totalPage, page));
    for (var i = 0;i < count;i++) {
        if (parseInt(i / ONE_PAGE_COUNT) + 1 == page)
            $(newsLis[i]).attr("style", "");
        else
            $(newsLis[i]).attr("style", "display: none");
    }
}

function homePage() {
    currPage = 1;
    scanAllForShow(currPage);
    setUICurrPage(currPage);
}

function nexePage() {
    var last = currPage;
    if (last == totalPage)
        return;

    scanAllForShow(++currPage);

    setUICurrPage(currPage);
}

function prevPage() {
    var next = currPage;
    if (next <= 1) 
        return;

    scanAllForShow(--currPage);

    setUICurrPage(currPage);
}

function lastPage() {
    currPage = totalPage;
    scanAllForShow(currPage);
    setUICurrPage(currPage);
}

function goToPage() {
    var target = $("#goToPage").val();
    if (target == undefined)
        target = currPage;
    target = Math.max(1, Math.min(totalPage, target));
    currPage = target;
    scanAllForShow(target);
    setUICurrPage(currPage);
    $("#goToPage").val("");
}

// 页面加载完成后调用此函数
function init() {
    newsLis = $("#news-lis").children();
    count = newsLis.length;
    totalPage = parseInt(count / ONE_PAGE_COUNT + ((count % ONE_PAGE_COUNT) == 0? 0 : 1));
    currPage = 1;
    setUICount(count);
    setUIPages(totalPage);
    setUICurrPage(currPage);
    scanAllForShow(currPage);
    // 注册点击函数
    $("#home").click(homePage);
    $("#prev").click(prevPage);
    $("#next").click(nexePage);
    $("#last").click(lastPage);
    $("#goTo").click(goToPage);

}

window.onload = function() {
    init();
}