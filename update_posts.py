#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动扫描 posts 文件夹中的 HTML 文件并更新 posts.json
使用方法: python update_posts.py
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

def extract_post_info(html_file_path):
    """从HTML文件中提取文章信息"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
        title = title_match.group(1).strip() if title_match else Path(html_file_path).stem
        
        # 提取日期
        date_match = re.search(r'<span class="post-date">(.*?)</span>', content)
        date = date_match.group(1).strip() if date_match else datetime.now().strftime('%Y年%m月%d日')
        
        # 提取分类
        category_match = re.search(r'<span class="post-category">(.*?)</span>', content)
        category = category_match.group(1).strip() if category_match else '未分类'
        
        # 提取摘要（从首页的excerpt或文章的第一段）
        excerpt_match = re.search(r'<p class="post-excerpt">(.*?)</p>', content)
        if not excerpt_match:
            # 尝试提取文章内容的第一段
            first_p_match = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
            if first_p_match:
                excerpt = first_p_match.group(1).strip()
                # 清理HTML标签
                excerpt = re.sub(r'<[^>]+>', '', excerpt)
                excerpt = excerpt[:150] + '...' if len(excerpt) > 150 else excerpt
            else:
                excerpt = '暂无摘要'
        else:
            excerpt = excerpt_match.group(1).strip()
            # 清理可能的HTML标签
            excerpt = re.sub(r'<[^>]+>', '', excerpt)
        
        return {
            'title': title,
            'filename': Path(html_file_path).name,
            'date': date,
            'category': category,
            'excerpt': excerpt
        }
    except Exception as e:
        print(f"处理文件 {html_file_path} 时出错: {e}")
        return None

def scan_posts_directory(posts_dir='posts'):
    """扫描posts目录，提取所有HTML文件的信息"""
    posts = []
    posts_path = Path(posts_dir)
    
    if not posts_path.exists():
        print(f"错误: {posts_dir} 目录不存在")
        return posts
    
    # 扫描所有HTML文件
    html_files = list(posts_path.glob('*.html'))
    
    if not html_files:
        print(f"警告: 在 {posts_dir} 目录中未找到HTML文件")
        return posts
    
    print(f"找到 {len(html_files)} 个HTML文件，开始处理...")
    
    for html_file in html_files:
        print(f"处理: {html_file.name}")
        post_info = extract_post_info(html_file)
        if post_info:
            posts.append(post_info)
    
    # 按日期排序（最新的在前）
    def parse_date_for_sort(date_str):
        try:
            match = re.match(r'(\d{4})年(\d{1,2})月(\d{1,2})日', date_str)
            if match:
                year, month, day = map(int, match.groups())
                return datetime(year, month, day)
        except:
            pass
        return datetime(1970, 1, 1)  # 默认日期
    
    posts.sort(key=lambda x: parse_date_for_sort(x['date']), reverse=True)
    
    return posts

def update_posts_json(posts, output_file='posts.json'):
    """更新posts.json文件"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False, indent=4)
        print(f"\n成功更新 {output_file}")
        print(f"共 {len(posts)} 篇文章")
        return True
    except Exception as e:
        print(f"错误: 无法写入 {output_file}: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("博客文章列表更新工具")
    print("=" * 50)
    
    # 扫描posts目录
    posts = scan_posts_directory('posts')
    
    if not posts:
        print("\n没有找到任何文章，请检查posts目录")
        return
    
    # 更新posts.json
    if update_posts_json(posts, 'posts.json'):
        print("\n更新完成！")
        print("\n文章列表:")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']} ({post['date']})")
    else:
        print("\n更新失败！")

if __name__ == '__main__':
    main()

