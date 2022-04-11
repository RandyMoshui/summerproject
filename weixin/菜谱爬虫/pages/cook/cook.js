// pages/cook/cook.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    array:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var arr = this.getData();
    this.setData({array:arr});
  },

  // 获取数据
  getData:function(){
    var arr = [];
    arr = [{
    img : 'https://st-cn.meishij.net/r/241/31/13695491/a13695491_162946355380483.jpg',
    title : '上海名菜四喜烤麸',
    collectNumber : 1089,
    browserNumber : "7.7万",
    },
    {
    img : 'https://st-cn.meishij.net/r/227/67/10016977/a10016977_162945246936019.jpg',
    title : '豆酱烧肉',
    collectNumber : 1089,
    browserNumber : "7.7万",
    },{
      img : 'https://st-cn.meishij.net/r/181/98/13899681/a13899681_162944700084672.jpg',
      title : '自制凉皮',
      collectNumber : 1089,
      browserNumber : "7.7万",
      }
  
  ];
    return arr;
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})