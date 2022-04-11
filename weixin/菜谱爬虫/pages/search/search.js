// pages/search/search.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    search_content:"",
    base_url:"https://so.meishi.cc/?q="
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  },
  search_input:function(e){
    this.setData({
      search_content: e.detail.value
    })
  },
  search_action:function(){
    var that = this
    wx.navigateTo({
      url: '/pages/jump/jump?flag=' + that.data.base_url + that.data.search_content
    })
  }
})