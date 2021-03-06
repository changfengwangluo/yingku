# -*- coding: utf-8 -*-
import scrapy
import html2text
from film import models as FM
from comment import models as CM
import re
from scrapy.selector import Selector
import requests


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/title/tt0371746/']

    # jianjie = models.TextField(verbose_name='汉语简介', default='')  # 短
    # juqing = models.TextField(verbose_name='汉语剧情', default='')  # 长
    # ejianjie = models.TextField(verbose_name='英语简介', default='')  # 短
    # ejuqing = models.TextField(verbose_name='英语剧情', default='')  # 长
    # jibie = models.TextField(verbose_name='电影级别', default='')

    # bianju = models.CharField(verbose_name='编剧', max_length=255, default='')
    # yanyuan = models.CharField(verbose_name='演员', max_length=255, default='')
    # guojia = models.CharField(verbose_name='国家', max_length=255, default='')

    # chupingongsi = models.CharField(verbose_name='出品公司', max_length=255, default='')
    # zhipiangongsi = models.CharField(verbose_name='制片公司', max_length=255, default='')
    # shichang = models.CharField(verbose_name='时长', max_length=255, default='')
    # zhipiandiqu = models.CharField(verbose_name='制片地区', max_length=255, default='')
    # chengben = models.CharField(verbose_name='制片成本', max_length=255, default='')
    # year = models.CharField(verbose_name='年代', max_length=255, default='')
    # paishedi = models.CharField(verbose_name='拍摄地点', max_length=255, default='')
    # duibai = models.CharField(verbose_name='对白语言', max_length=255, default='')
    # paisheriqi = models.CharField(verbose_name='拍摄日期', max_length=255, default='')
    # secai = models.CharField(verbose_name='色彩', max_length=255, default='')
    # imdb = models.CharField(verbose_name='IMDB编码', max_length=255, default='')
    # add_time = models.DateField(verbose_name='收录时间', default=datetime.now)
    # misuc = models.CharField(verbose_name='电影原声', max_length=255, default='')
    # db_fen = models.IntegerField(verbose_name='豆瓣评分', default=0)

    # youku = models.TextField(verbose_name='优酷地址', default='')
    # bilibili = models.TextField(verbose_name='bilibili地址', default='')
    # aiqiyi = models.TextField(verbose_name='爱奇艺', default='')

    def parse(self, response):

        ename = response.xpath('//h1/text()').extract_first()  # 英文名

        imdb_fen = float(response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first())  # imdb评分

        year = response.xpath('//span[@id="titleYear"]/a/text()').extract_first()  # 年代
        jibie = response.xpath(
            '//div[@class="title_wrapper"]/div[@class="subtext"]/meta/@content').extract_first()  # 电影级别
        shichang = html2text.html2text(
            response.xpath('//div[@class="title_wrapper"]/div[@class="subtext"]/time/text()').extract_first())  # 时长
        category_list = response.xpath(
            '//div[@class="title_wrapper"]/div[@class="subtext"]/a[contains(@href,"genre")]/span/text()').extract()  # 电影类型【list】
        # 处理电影分类
        category = self.trans_category(category_list)
        guojia = response.xpath(
            '//div[@id="titleDetails"]/div[@class="txt-block"]/a[contains(@href,"country")]/text()').extract_first()  # 国家/地区
        duibai_list = response.xpath(
            '//div[@id="titleDetails"]/div[@class="txt-block"]/a[contains(@href,"primary_language")]/text()').extract()  # 对白语言
        duibai = ','.join(duibai_list)
        # 如果已经存在会报错，需要处理
        # FM.Info.objects.create(
        #     ename=ename,
        #     name=name,
        #     imdb_fen=imdb_fen,
        #     year=year,
        #     jibie=jibie,
        #     shichang=shichang,
        #     category=category,
        #     guojia=guojia,
        #     duibai=duibai,
        # )

        # 摘要+剧情;meta携带参数--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/plotsummary', callback=self.plotsummary,
        # meta={'film_name': ename})

        # 译名+发布国家/日期--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/releaseinfo', callback=self.releaseinfo,
        # meta={'film_name': ename})

        ##整个制作团队（导演，编剧，演员……--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/fullcredits', callback=self.fullcredits,
        # meta={'film_name': ename})

        # 拍摄地+拍摄日期--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/locations', callback=self.locations,
        # meta={'film_name': ename})

        # 穿帮--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/goofs', callback=self.goofs,
        #                      meta={'film_name': ename})

        # 用户评论--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/reviews', callback=self.reviews,
        # meta={'film_name': ename, 'data-ajaxurl': ''})  # 'data-ajaxurl'最开始地时候是赋予空值

        # 用户评论--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/trivia', callback=self.trivia,
        #                      meta={'film_name': ename})
        # 问答
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/faq', callback=self.faq,
        #                      meta={'film_name': ename})

        # 技术规格采集不完整，对用户也作用不大，暂时不采集。

        # 支持公司--ok
        # yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/companycredits', callback=self.companycredits,
        #                      meta={'film_name': ename})

        # 支持公司--ok
        yield scrapy.Request(url='https://www.imdb.com/title/tt0371746/parentalguide', callback=self.parentalguide,
                             meta={'film_name': ename})

    # 逐个翻译电影分类，返回一个带格式的字符串
    def trans_category(self, category_list):
        trans_list = []
        for category_name in category_list:
            # 翻译对应的电影分类名
            if category_name == 'Action':
                category_name = '动作'
            elif category_name == 'Adventure':
                category_name = '冒险'
            elif category_name == 'Sci-Fi':
                category_name = '科幻'
            trans_list.append(category_name)

        return ','.join(trans_list)

    # 摘要+剧情
    def plotsummary(self, response):
        film_name = response.meta['film_name']
        zy_list = response.xpath(
            '//ul[@id="plot-summaries-content"]/li[@class="ipl-zebra-list__item"]/p/text()').extract()
        for li in zy_list:
            FM.ZhaiYao.objects.create(
                film=film_name,
                content=li,
            )
        juqing = response.xpath('//ul[@id="plot-synopsis-content"]/li[@class="ipl-zebra-list__item"]').extract_first()
        juqing = html2text.html2text(juqing)
        FM.Info.objects.filter(ename=film_name).update(juqing=juqing)

    # 拍摄地+日期
    def locations(self, response):
        film_name = response.meta['film_name']
        psd_list = response.xpath('//section[@id="filming_locations"]/div[contains(@class,"soda")]').extract()
        for li in psd_list:
            address = Selector(text=li).xpath('//dt/a/text()').extract_first()
            changjing = Selector(text=li).xpath('//dd/text()').extract_first()

            FM.PaiSheDi.objects.create(
                film=film_name,
                address=address,
                changjing=changjing,
            )

        paisheriqi = response.xpath('//section[@id="filming_dates"]/ul/li/text()').extract_first()
        FM.Info.objects.filter(ename=film_name).update(paisheriqi=paisheriqi)

    # 译名+发布国家/日期
    def releaseinfo(self, response):
        film_name = response.meta['film_name']
        shangying_list = response.xpath('//table[@id="release_dates"]/tr').extract()
        # 国家/地区+上映日期+城市
        for li in shangying_list:
            '''
            '<tr class="odd">
            <td><a href="/calendar/?region=au&amp;ref_=ttrel_rel_1">Australia</a></td>
            <td class="release_date">14 April 2008</td>
            <td> (Sydney)
 (premiere)</td>
        </tr>'
            '''
            guojia = Selector(text=li).xpath('//td/a/text()').extract_first()
            shijian = Selector(text=li).xpath('//td[@class="release_date"]/text()').extract_first()
            chengshi = Selector(text=li).xpath('//td[last()]/text()').extract_first()
            FM.ShangYing.objects.create(
                film=film_name,
                guojia=guojia,
                chengshi=chengshi,
                shijian=shijian,
            )
            # 译名/别名
            yiming_list = response.xpath('//table[@id="akas"]/tr').extract()
            '''
            <tr class="odd">
                        <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">阿根廷</font></font></td>
                        <td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">铁人 - 铁人</font></font></td>
                    </tr>
            '''
            for li in yiming_list:
                guojia = Selector(text=li).xpath('//td[last()-1]/text()').extract_first()
                yiming = Selector(text=li).xpath('//td[last()]/text()').extract_first()

                FM.YiMing.objects.create(
                    film=film_name,
                    guojia=guojia,
                    name=yiming,
                )

    # 整个制作团队（导演，编剧，演员……）
    def fullcredits(self, response):
        film_name = response.meta['film_name']
        category_tuple = FM.YanZhiYuan.CG  # 演职人员分类
        for category in category_tuple:
            if category[0] == 'yy':
                flag = 'Cast'  # 演员
            elif category[0] == 'dy':
                flag = 'Directed'  # 导演
            elif category[0] == 'bj':
                flag = 'Writing Credits'  # 编剧
            elif category[0] == 'zp':
                flag = 'Produced by'  # 制片人
            elif category[0] == 'ms':
                flag = 'Music by'  # 音乐
            elif category[0] == 'sy':
                flag = 'Cinematography by'  # 摄影
            elif category[0] == 'jj':
                flag = 'Film Editing by'  # 剪辑
            elif category[0] == 'tx':
                flag = 'Casting By'  # 角色挑选
            elif category[0] == 'zp':
                flag = 'Production Design'  # 制片设计
            elif category[0] == 'hz':
                flag = 'Makeup Department'  # 化妆
            elif category[0] == 'sc':
                flag = 'Production Management'  # 生产管理
            elif category[0] == 'zl':
                flag = 'Second Unit Director'  # 助理导演
            elif category[0] == 'ad':
                flag = 'Art Department'  # 美术
            elif category[0] == 'yx':
                flag = 'Sound Department'  # 音效
            elif category[0] == 'tx':
                flag = 'Special Effects'  # 特效
            elif category[0] == 'sj':
                flag = 'Visual Effects'  # 视觉
            elif category[0] == 'tj':
                flag = 'Stunts'  # 特技
            elif category[0] == 'dj':
                flag = 'Electrical Department'  # 道具场工
            elif category[0] == 'dh':
                flag = 'Animation Department'  # 动画
            elif category[0] == 'dp':
                flag = 'Casting Department'  # 底片冲印
            elif category[0] == 'fz':
                flag = 'Costume and Wardrobe'  # 服装管理
            elif category[0] == 'zb':
                flag = 'Editorial Department'  # 编辑助理
            elif category[0] == 'cj':
                flag = 'Location Management'  # 场景管理
            elif category[0] == 'md':
                flag = 'Music Department'  # 音乐部门
            elif category[0] == 'ys':
                flag = 'Transportation Department'  # 底片运送
            elif category[0] == 'qt':
                flag = 'Other crew'  # 其他职员

            if category[0] == 'yy':
                xpath_text = '//h4[@id="cast"]/following-sibling::table[1]/tr'
            else:
                xpath_text = '//h4[contains(text(),"%s")]/following-sibling::table[1]/tbody/tr' % flag
            # /td/a/text()
            person_list = response.xpath(xpath_text).extract()
            for li in person_list:
                if category[0] == 'yy':
                    image_url = Selector(text=li).xpath('//td[@class="primary_photo"]/a/img/@loadlate').extract_first()
                    if image_url is None:
                        image_url = Selector(text=li).xpath(
                            '//td[@class="primary_photo"]/a/img/@src').extract_first()
                    ename = Selector(text=li).xpath('//td[@class="itemprop"]/a/span/text()').extract_first()
                    # 已超链接存在地情况
                    beizhu = Selector(text=li).xpath('//td[@class="character"]/a/text()').extract_first()  # 获取一个就好了。
                    if beizhu is None:
                        beizhu = Selector(text=li).xpath('//td[@class="character"]/text()').extract_first()  # 直接获取备注名
                        if beizhu is not None:
                            beizhu = re.sub('\n', '', beizhu).lstrip().rstrip()
                else:
                    ename = Selector(text=li).xpath('//td[@class="name"]/a/text()').extract_first()
                    beizhu = Selector(text=li).xpath('//td[@class="credit"]/text()').extract_first()
                    if beizhu is None:
                        beizhu = ''

                if ename is not None:
                    FM.YanZhiYuan.objects.create(
                        film=film_name,
                        ename=ename,
                        category=category[0],
                        image=image_url,
                        beizhu=beizhu
                    )

    # 穿帮镜头
    def goofs(self, response):
        film_name = response.meta['film_name']

        jumpto_list = response.xpath('//div[@class="jumpto"]/a/text()').extract()
        for li in jumpto_list:  # li就是穿帮的类型了
            # count是此穿帮类型下，穿帮的数量
            count = response.xpath(
                '//div[@class="jumpto"]/a[contains(text(),"' + li + '")]/following-sibling::text()').extract_first()
            count = re.findall('\d+', count)[0]
            xq_list = response.xpath('//h4[contains(text(),"' + li + '")]/following-sibling::div').extract()[
                      0:int(count)]
            for xq in xq_list:
                xq_content = Selector(text=xq).xpath('//div[@class="sodatext"]/text()').extract_first()
                FM.ChuanBang.objects.create(
                    film=film_name,
                    category=li,
                    xiangqing=xq_content,
                )

    # 电影评论
    def reviews(self, response):
        film_name = response.meta['film_name']
        data_ajaxurl = response.meta['data-ajaxurl']
        # <div class="load-more-data" data-key="fqcavm4i2jhknxl2aqshhc4qqloiff4blygkdnmgqufie5q7nt257gcbtnecfy6gygunmfmoyyw3o" data-ajaxurl="/title/tt1300854/reviews/_ajax?sort=helpfulnessScore&dir=desc">
        data_key = response.xpath('//div[@class="load-more-data"]/@data-key').extract_first()
        if data_ajaxurl == '':
            data_ajaxurl = response.xpath('//div[@class="load-more-data"]/@data-ajaxurl').extract_first()

        lister_list = response.xpath('//div[contains(@class,"text show-more__control")]/text()').extract()

        for lister in lister_list:
            CM.FilmComments.objects.create(
                film=film_name,
                content=lister,
            )
        if len(lister_list) > 0:
            yield scrapy.Request(
                url='https://www.imdb.com%s?sort=helpfulnessScore&dir=desc&ref_=undefined&paginationKey=%s' % (
                    data_ajaxurl, data_key), callback=self.reviews,
                meta={'film_name': film_name, 'data-ajaxurl': data_ajaxurl})

    # 幕后花絮
    def trivia(self, response):
        film_name = response.meta['film_name']
        huaxu_list = response.xpath('//div[@class="sodatext"]').extract()
        for huaxu in huaxu_list:
            huaxu = html2text.html2text(huaxu)
            huaxu = re.sub('\(\/name\/.+?\)|\(\/title\/.+?\)', '', huaxu)
            FM.HuaXu.objects.create(
                film=film_name,
                huaxu=huaxu,
            )

    # 问答
    def faq(self, response):
        film_name = response.meta['film_name']
        faq_list = response.xpath('//section[@id="faq-answered"]/ul/li').extract()

        for faq in faq_list:
            question = Selector(text=faq).xpath('//div[@class="faq-question-text"]/text()').extract_first()
            anwser = Selector(text=faq).xpath('//section/div[last()]/p').extract_first()
            anwser = html2text.html2text(anwser)
            anwser = re.sub('\(\/name\/.+?\)|\(\/title\/.+?\)', '', anwser)

            FM.WenDa.objects.create(
                film=film_name,
                wen=question,
                da=anwser,
            )

    # 支持+合作公司
    def companycredits(self, response):
        film_name = response.meta['film_name']
        cg_list = response.xpath('//h4[@class="dataHeaderWithBorder"]/text()').extract()
        for cg in cg_list:
            if cg == 'Production Companies':
                category = '生产公司'
                id = 'production'
            elif cg == 'Distributors':
                category = '分销商'
                id = 'distributors'
            elif cg == 'Special Effects':
                category = '特殊效果'
                id = 'specialEffects'
            elif cg == 'Other Companies':
                category = '其他公司'
                id = 'other'
            else:
                category = ''
                id = ''

            sc_list = response.xpath('//h4[@id="' + id + '"]/following-sibling::ul[1]/li').extract()
            for sc in sc_list:
                name = Selector(text=sc).xpath('string(.)').extract_first()
                name = re.sub('\n', '', name).strip()
                name = re.sub('\s{2,}', ' ', name).strip()

                FM.GongSi.objects.create(
                    film=film_name,
                    category=category,
                    name=name
                )

    # 家长指南(政治/色情/暴力等少儿不宜内容)
    def parentalguide(self, response):
        film_name = response.meta['film_name']
        # 电影评级
        mpaa = response.xpath('//*[@id="mpaa-rating"]/td[2]/text()').extract_first()  # imdb的总体评级
        FM.ZhiNan.objects.create(
            film=film_name,
            category='IMDB评级',
            desc=mpaa,
        )
        Certification = response.xpath('//*[@id="certifications-list"]/td[2]/ul/li').xpath(
            'string(.)').extract()  # 各个国家/地区地评级详情

        for cc in Certification:
            cc = re.sub('\n', '', cc)
            cc = re.sub('\s{2,}', ' ', cc)

            FM.ZhiNan.objects.create(
                film=film_name,
                category='国家/地区评级',
                desc=cc,
            )

        desc_name_list = response.xpath(
            '//section[contains(@id,"advisory")]/@id').extract()#这里要根据id来做,下面的代码需要做一定地修改

        for desc_name in desc_name_list:
            if desc_name == 'Sex & Nudity':
                category = '性与裸体'
                id = 'advisory-nudity'
            elif desc_name == 'Violence & Gore':
                category = '暴力与血腥'
                id = 'advisory-violence'
            elif desc_name == 'Profanity':
                category = '亵渎'
                id = 'advisory-profanity'
            elif desc_name == 'Alcohol, Drugs & Smoking':
                category = '酒精/毒品/吸烟'
                id = 'advisory-alcohol'
            elif desc_name == 'Frightening & Intense Scenes':
                category = '惊恐场面'
                id = 'advisory-frightening'
            else:
                id = 'advisory-spoilers'#剧透

            desc_list = response.xpath(
                '//section[@id="' + id + '"]/ul/li[@class="ipl-zebra-list__item"]/text()').extract()

            for desc in desc_list:
                desc = re.sub('\n', '', desc)
                desc = re.sub('\s{2,}', ' ', desc)
                if desc != ' ':
                    FM.ZhiNan.objects.create(
                        film=film_name,
                        category=category,
                        desc=desc,
                    )
